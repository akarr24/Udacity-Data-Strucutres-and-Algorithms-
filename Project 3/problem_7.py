# -*- coding: utf-8 -*-
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        i = 0
        while i < len(path):
            elem = path[i]
            node = node.insert(elem)
            i += 1
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        i = 0
        while i < len(path):
            elem = path[i]
            if elem in node.children.keys():
                node = node.children[elem]
                i += 1
            else:
                return None
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, elem):
        # Insert the node as before
        if elem not in self.children.keys():
            child = RouteTrieNode()
            self.children[elem] = child
            return child
        return self.children[elem]

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,root_handler, handler_not_found):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler)
        self.handler_not_found = handler_not_found

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        result = self.trie.find(self.split_path(path))
        if not result:
            return self.handler_not_found
        return result


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        stripped_path = path.strip('/')
        if stripped_path:
            return stripped_path.split('/')
        return []


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


router.add_handler("/home", "base")
router.add_handler("/home/contact", "office")
router.add_handler("/home/contact/bangalore", "bangalore handler")
router.add_handler("/home/contact/Mumbai", "Mumbai contact handler")


print(router.lookup("/home"))

print(router.lookup("/home/contact"))

print(router.lookup("/home/contact/bangalore"))

print(router.lookup("/home/contact/Mumbai"))

