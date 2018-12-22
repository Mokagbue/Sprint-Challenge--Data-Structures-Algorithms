class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# a.k.a Inorder
  def depth_first_for_each(self, cb):
    # Recursive Implemenetation
    # call the call-back first, process the current node
    cb(self.value)
    # process the left side, then the right
    if self.left:
      self.left.depth_first_for_each(cb)
    if self.right:
      self.right.depth_first_for_each(cb)

  # # Iterative Implementation
  # def depth_first_for_each(self, cb):
  #   stack = []
  #   stack.append(self)
  #   while len(stack):
  #     current = stack.pop()
  #     if current_node.right:
  #       stack.append(current_node.right)
  #     if current_node.left:
  #       stack.append(current_node.left)
  #     cb(current_node.value)
 
# a.k.a Level Order
  def breadth_first_for_each(self, cb):
    q = []
    q.append(self)
    
    while len(q):
      current_node = q.pop(0)
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)
      cb(current_node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

#we are finding the height of the tree, 
# so we know how many levels there are
#this will help when we try to grab nodes 
# at specific levels = (for breadth first traversal)
  def height(self, node):
    if node is None:
      return 0
    else:
      left_height = height(node.left)
      right_height = height(node.right)

      if left_height > right_height:
        return left_height + 1
      else:
        return right_height + 1
