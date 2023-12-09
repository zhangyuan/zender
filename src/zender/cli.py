import click
import glob
import zender


@click.command()
@click.option(
    "--templates_directory",
    default="./templates",
    help="The path to templates directory",
)
@click.option(
    "--target_directory", default="./target", help="The directory to output directory"
)
def render(templates_directory, target_directory):
    metadata_store = zender.MetadataStore()
    compiler = zender.Compiler(
        search_directory=templates_directory,
        target_path=target_directory,
        metadata_store=metadata_store,
    )

    if templates_directory[-1] == "/":
        templates_directory = templates_directory[:-1]

    for file in glob.glob(f"{templates_directory}/**/*", recursive=True):
        print(f"file:{file}")
        file = file[len(templates_directory) + 1 :]
        compiler.compile(file)
    compiler.save_metadata()

def main():
    # pylint: disable=no-value-for-parameter
    render()

if __name__ == "__main__":
    main()
