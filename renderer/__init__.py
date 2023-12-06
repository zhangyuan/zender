import os
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class Lineage:
    def __init__(self, source_code) -> None:
        self.source_code = source_code
        self.targets = []
        self.sources = []

    def source(self, dependence):
        if dependence not in self.sources:
            self.sources.append(dependence)

        return dependence

    def target(self, target):
        if target not in self.targets:
            self.targets.append(target)
        return target

    def as_dict(self):
        return {
            "source_code": self.source_code,
            "targets": self.targets,
            "sources": self.sources,
        }

    def __str__(self):
        return json.dumps(self.__dict__)


class MetadataStore:
    def __init__(self) -> None:
        self.lineage: [Lineage] = []

    def add_lineage(self, lineage: Lineage):
        self.lineage.append(lineage)

    def to_json(self):
        return json.dumps(
            {"lineage": [lineage.as_dict() for lineage in self.lineage]}, indent=4
        )


class Compiler:
    def __init__(
        self, search_directory, target_path: str, metadata_store: MetadataStore
    ) -> None:
        self.env = Environment(
            loader=FileSystemLoader(search_directory), autoescape=False
        )
        self.target_directory = target_path
        self.metadata_store = metadata_store

    def compile(self, model_path):
        lineage = Lineage(model_path)
        func_dict = {
            "source": lineage.source,
            "target": lineage.target,
        }

        template = self.env.get_template(model_path)
        template.globals.update(func_dict)

        content = template.render()

        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

        target_file_path = Path(
            os.path.join(self.target_directory, "compiled", model_path)
        )
        target_file_directory = target_file_path.parent

        if not os.path.exists(target_file_directory):
            os.makedirs(target_file_directory)

        with open(target_file_path, "w", encoding="utf-8") as f:
            f.write(content)

        self.metadata_store.add_lineage(lineage=lineage)

    def save_metadata(self):
        metadata_store_path = os.path.join(self.target_directory, "metadata.json")
        with open(metadata_store_path, "w", encoding="utf-8") as f:
            f.write(self.metadata_store.to_json())


def compile_models(models, search_directory=None, target_path="target"):
    if not search_directory:
        search_directory = ["templates"]
    metadata_store = MetadataStore()
    compiler = Compiler(
        search_directory=search_directory,
        target_path=target_path,
        metadata_store=metadata_store,
    )

    for model in models:
        compiler.compile(model)
    compiler.save_metadata()
