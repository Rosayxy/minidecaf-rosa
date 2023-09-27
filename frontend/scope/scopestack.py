from typing import Optional
from frontend.scope.globalscope import GlobalScopeType
from frontend.symbol.symbol import Symbol

from .scope import Scope,ScopeKind

class ScopeStack:
    def __init__(self):
        self.stack=[]
        self.loop=[]
    def push(self,scope:Scope):
        self.stack.append(scope)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def lookup(self,name:str)->Optional[Symbol]:
        for i in reversed(self.stack):
            if i.containsKey(name):
                return i.get(name)    
        return None
    def pushloop(self,scope:Scope):
        self.stack.append(scope)
        self.loop.append(scope)
    def poploop(self):
        self.stack.pop()
        return self.loop.pop()
    def toploop(self):
        return self.loop[-1]