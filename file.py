
from posixpath import split
from functools import wraps
# https://github.com/DaftAcademy-Python-LevelUP-Dev-2022/2_a-jak-art-aturant


def greeter(fun_to_decorate):
    def inner_wrapper(*fun_args, **fun_kwargs):
        result = 'aloha ' + fun_to_decorate(*fun_args, **fun_kwargs)
        result =' '.join([x.capitalize() for x in result.split(' ')])
        return result
    return inner_wrapper

def sums_of_str_elements_are_equal(fun_to_decorate):    
    def inner_wrapper(*fun_args, **fun_kwargs):
        
        def sum_of_digits(in_str:str):
            t = sum([int(x) for x in in_str 
                        if x.isdigit()])
            t *= (-1 if in_str[0]=='-' else 1)      
            return str(t)
        tmp = fun_to_decorate(*fun_args, **fun_kwargs)
        s_tmp = [sum_of_digits(x) for x in tmp.split(' ')]
        sep = ' == ' if len({*s_tmp}) == 1 else ' != '
        result = sep.join(s_tmp)
        return result
    
    return inner_wrapper

def format_output(*required_keys):
    def outer_wrapper(fun_to_wrap):
        def inner_wrapper(*fun_args, **fun_kwargs):
            tmp = fun_to_wrap(*fun_args, **fun_kwargs)
            assert isinstance(tmp,dict)
            ret=dict()
            
            for k in required_keys:
                _v = []
                for y in k.split('__'):
                    if y not in tmp.keys():
                        raise ValueError()
                    _v.append(tmp[y] if tmp[y] != '' else 'Empty value')
                ret[k] = ' '.join(_v)
            
            
            return ret
        return inner_wrapper
    return outer_wrapper
                

def add_method_to_instance(klass):
    def outer_wrapper(fun_to_decorate):
        @wraps(fun_to_decorate)
        def inner_wrapper(*args, **kwargs):
            return fun_to_decorate()
        setattr(klass,inner_wrapper.__name__,inner_wrapper )
        return getattr(klass, fun_to_decorate.__name__)
        
        return inner_wrapper
    return outer_wrapper