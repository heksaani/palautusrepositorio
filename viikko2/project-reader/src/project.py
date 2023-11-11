class Project:
    def __init__(self, name, licence, authors:list, description, dependencies, dev_dependencies):
        self.name = name
        self.license = licence
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        

    def _stringify_dependencies(self, dependencies):
        return "\n - ".join(dependencies) + "\n" if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}" + "\n"
            f"\nAuthors:\n - {self._stringify_dependencies(self.authors)}"
            f"\nDependencies:\n - {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
