import pkgutil

class Autoloader:
    # Load all application controllers
    entrypoint = "routes"
    admin_folder = "admin"

    def __init__(self, base_path, base_name):
        self.base_path = base_path
        self.base_name = base_name

        self.load_all()

    def load_all(self):
        for importer, module, ispkg in pkgutil.iter_modules(self.base_path):
            if ispkg:
                # Load normal route
                self.load_package("%s.%s.%s" % (self.base_name, module, self.entrypoint))

                # Load admin routes
                if self.package_exists("%s.%s.%s" % (self.base_name, module, self.admin_folder)):
                    self.load_package("%s.%s.%s.%s" % (self.base_name, module, self.admin_folder, self.entrypoint))

    def load_package(self, package):
        if self.package_exists(package):
            __import__(package)

    def package_exists(self, package):
        return pkgutil.find_loader(package) is not None
