from distutils.core import setup

setup(
    name='ColabPlugin',
    version='1.0',
    author='Blind',
    author_email='blind',
    py_modules=['plugin', 'cuda.cuda', 'c.c', 'cpp.cpp', 'verilog.verilog', 'java.java', 'gem5.gem5', 'valgrind.valgrind', 'llvm.llvm', 'rust.rust', 'common.helper', 'common.tool'],
    url='https://github.com/blindreviewsrc',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA, C/C++, GCC code, Verilog, LLVM, Gem5',
    # long_description=open('README.md').read(),
)
