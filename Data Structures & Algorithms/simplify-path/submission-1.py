class Solution:
    def simplifyPath(self, path: str) -> str:
        # Step 1: Split the input 'path' string into individual components (directory or file names).
        # The path is split using the '/' character as a delimiter.
        # This will result in a list that may contain empty strings (from consecutive slashes like "//"),
        # single dots ('.'), double dots ('..'), and actual directory/file names.
        path_segments = path.split('/')

        # Step 2: Initialize a stack to build the simplified path.
        # This 'path_stack' will store only the valid directory names that should be
        # part of the canonical path, in the correct order. It effectively simulates
        # navigating through the file system.
        path_stack = []

        # Step 3: Iterate through each 'segment' obtained from splitting the path.
        # We process each segment to decide how it affects the current path.
        for segment in path_segments:
            # Condition A: Handle '.' (current directory) or empty strings (from consecutive slashes).
            # If a 'segment' is a single period '.', it represents the current directory,
            # which does not change the path and should be ignored in the simplified path.
            # If a 'segment' is an empty string (e.g., from "//" or a trailing "/"),
            # it also does not represent a valid directory name in the canonical path and should be ignored.
            if segment == '.' or segment == '':
                continue # Skip to the next segment without modifying the stack.

            # Condition B: Handle '..' (parent directory).
            # If a 'segment' is a double period '..', it represents navigating up to the parent directory.
            elif segment == '..':
                # If the 'path_stack' is not empty, it means there is a parent directory
                # to go back to. So, we pop the last directory from the stack.
                if path_stack:
                    path_stack.pop()
                # If the 'path_stack' is empty (meaning we are already at the root or above),
                # attempting to go up '..' further does not change the path, so we do nothing.
                # The root directory is the highest level, and '..' from '/' still results in '/'.
            # Condition C: Handle valid directory or file names.
            # If the 'segment' is neither '.', '..', nor an empty string, it must be a valid
            # directory or file name (e.g., "home", "...", "folder_name").
            else:
                # Add this valid directory/file name to the 'path_stack'.
                # This effectively navigates into this directory.
                path_stack.append(segment)

        # Step 4: Construct the final simplified canonical path from the 'path_stack'.
        # If the 'path_stack' is empty after processing all segments, it means the
        # simplified path is the root directory '/'.
        if not path_stack:
            return '/'
        # If the 'path_stack' is not empty, join the directory names stored in it
        # with a single '/' as a separator, and prepend a '/' to make it an absolute path.
        # This correctly forms the canonical path (e.g., "/home/user").
        return '/' + '/'.join(path_stack)