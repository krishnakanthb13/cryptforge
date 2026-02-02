import importlib
import pkgutil
import inspect
import sys
import os
from typing import Dict, Type
import logics
from logics.base import EncryptionLogic

def load_logics() -> Dict[str, Type[EncryptionLogic]]:
    """
    Dynamically discovers and loads all encryption logic plugins
    from the 'logics' package.
    
    Returns:
        Dict[str, Type[EncryptionLogic]]: A dictionary mapping logic names to their classes.
    """
    discovered_logics = {}
    
    # Iterate over all modules in the logics package
    package_path = os.path.dirname(logics.__file__)
    
    for _, module_name, _ in pkgutil.iter_modules([package_path]):
        if module_name == 'base':
            continue
            
        try:
            # Import the module
            module = importlib.import_module(f'logics.{module_name}')
            
            # Inspect the module for classes that inherit from EncryptionLogic
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    issubclass(obj, EncryptionLogic) and 
                    obj is not EncryptionLogic):
                    
                    # Instantiate to get the name property (or check if it's a property)
                    # We expect the class to have a 'name' attribute or property.
                    # Ideally we should instantiate it later, but for discovery we can check attributes.
                    # For safety, let's assume we instantiate it when used, but here we need the name key.
                    # Let's instantiate a temporary instance to get the name, 
                    # OR require a static 'name' field. 
                    # The base class has @property abstractmethod.
                    # Let's try to instantiate it. If it fails (requires args), we might need a different design.
                    # For now, we assume __init__ takes no arguments.
                    
                    try:
                        instance = obj()
                        logic_name = instance.name
                        discovered_logics[logic_name] = obj
                    except Exception as e:
                        print(f"Warning: Failed to instantiate logic {name} in {module_name}: {e}")
                        
        except Exception as e:
            print(f"Warning: Failed to load module {module_name}: {e}")
            
    return discovered_logics
