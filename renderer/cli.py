import click


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
    click.echo(f"{templates_directory}, {target_directory}")


if __name__ == "__main__":
    render()
