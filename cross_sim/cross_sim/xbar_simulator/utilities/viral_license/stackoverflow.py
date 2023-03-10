'''
Contains all code snippets taken from StackOverflow

Which are licensed under CC-BY-SA http://creativecommons.org/licenses/by-sa/3.0/
'''
from abc import ABCMeta

__all__ = ['DocStringInheritorAbstractBaseClass']

class DocStringInheritorAbstractBaseClass(ABCMeta):
    '''
    A metaclass that allows subclasses to inherit docstrings from superclasses
    
    The main reason that this is used is so that docstrings get propagated to subclasses when documentation is being automatically generated by sphinx.
    
    A variation on
    http://groups.google.com/group/comp.lang.python/msg/26f7b4fcb4d66c95
    by Paul McGuire
    
    Taken from http://stackoverflow.com/a/8101118
    '''
    def __new__(cls, name, bases, clsdict):
        if not('__doc__' in clsdict and clsdict['__doc__']):
            for mro_cls in (mro_cls for base in bases for mro_cls in base.mro()):
                doc=mro_cls.__doc__
                if doc:
                    clsdict['__doc__']=doc
                    break
        for attr, attribute in clsdict.items():
            if not attribute.__doc__:
                for mro_cls in (mro_cls for base in bases for mro_cls in base.mro()
                                if hasattr(mro_cls, attr)):
                    doc=getattr(getattr(mro_cls,attr),'__doc__')
                    if doc:
                        attribute.__doc__=doc
                        break
        return type.__new__(cls, name, bases, clsdict)
