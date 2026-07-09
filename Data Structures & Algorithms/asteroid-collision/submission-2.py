class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:

            while stack and stack[-1] > 0 and ast < 0:

                top_ast = stack[-1]
                cur_ast = abs(ast)
            
                if top_ast > cur_ast:
                    ast = 0
                    break
                
                elif cur_ast > top_ast:
                    stack.pop()
                
                else:
                    stack.pop()
                    ast = 0
                    break
            
            if ast != 0:
                stack.append(ast)
        
        return stack