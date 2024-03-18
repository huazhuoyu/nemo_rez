import os
import shutil
from rezbuild import BuilderBase

variant_map = {
    '0': 'maya-2018',
    '1': 'maya-2019',
    '2': 'maya-2020',
    '3': 'maya-2022',
    '4': 'maya-2023',
    '5': 'maya-2024'
}


class CustomBuilder(BuilderBase):
    def before_build(self, builder_dir):
        self.package_root = self.root
        self.root = os.path.join(
            self.root, variant_map[os.getenv('REZ_BUILD_VARIANT_INDEX')]
        )

    def copytree(self, builder_dir, src, dst):
        shutil.copytree(os.path.join(self.package_root, 'Nemo', src),
                        os.path.join(builder_dir, dst))

    def after_build(self, builder_dir):
        version = os.path.basename(builder_dir).split('-')[-1]
        self.copytree(builder_dir, 'scripts', 'scripts')
        self.copytree(builder_dir, 'modules', 'modules')
        self.copytree(builder_dir, 'depends/windows', 'depends')
        self.copytree(builder_dir, 'lib/windows-{}'.format(version), 'lib')
        self.copytree(
            builder_dir, 'plug-ins/windows-{}'.format(version), 'plug-ins')


def build():
    # need download nemo
    
    builder = CustomBuilder()
    builder.build()
