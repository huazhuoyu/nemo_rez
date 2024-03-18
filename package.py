"""The definition file of a Rez package."""

name = 'nemo'
authors = ['yuhuazhuo']
description = 'https://www.nemopuppet.com'
uuid = 'nemo.rez.yuhuazhuo'

requires = []

variants = [
    ['maya-2018'],
    ['maya-2019'],
    ['maya-2020'],
    ['maya-2022'],
    ['maya-2023'],
    ['maya-2024']
]

tests ={}


def commands():
    """
    MAYAVERSION:2020 PLATFORM:win64 Nemo 1.0 ./Nemo
    plug-ins: plug-ins/windows-2020
    scripts: ./scripts
    MAYA_CUSTOM_TEMPLATE_PATH+:= ui_templates
    NEMO_MODULES:= modules
    PATH+:= depends/windows
    PYTHONPATH+:= lib/windows-2020
    PYTHONPATH+:= extern
    :return:

    #hide menu
    NEMO_LOAD_TOPMENU=0
    """

    env.PYTHONPATH.append('{root}/scripts')
    env.PYTHONPATH.append('{root}/lib')

    env.MAYA_PLUG_IN_PATH.prepend('{root}/plug-ins')
    env.MAYA_SCRIPT_PATH.prepend('{root}/scripts')
    env.MAYA_CUSTOM_TEMPLATE_PATH.prepend('{root}/ui_templates')
    env.NEMO_MODULES = '{root}/modules'
    env.PATH.prepend('{root}/depends')


