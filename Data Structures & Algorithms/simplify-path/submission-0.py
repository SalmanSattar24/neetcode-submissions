class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_components = path.split('/')
        stack = []

        for component in path_components:

            if component == '.' or component == '':
                continue
            
            elif component == '..':
                if stack:
                    stack.pop()
            
            else:
                stack.append(component)
        

        if not stack:
            return '/'
        
        return '/' + '/'.join(stack)