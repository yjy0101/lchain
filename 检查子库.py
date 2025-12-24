import langchain_classic
import pkgutil

# 列出 langchain_classic 下的所有子模块
for importer, modname, ispkg in pkgutil.iter_modules(langchain_classic.__path__):
    print(modname)