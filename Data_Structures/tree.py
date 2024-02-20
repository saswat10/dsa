class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None

  def addChild(self, child):
    child.parent = self
    self.children.append(child)

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    
    return level
  
  def print_tree(self):
    spaces = ' ' * self.get_level() * 3
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()

  def print_tree_level(self, level):
    if self.get_level() > level:
      return
    spaces = ' ' * self.get_level() * 3
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree_level(level)


def build_product_tree():
  root = TreeNode('Electronics')


  laptop = TreeNode('Laptop')
  laptop.addChild(TreeNode('surfacebook'))
  laptop.addChild(TreeNode('pangolin'))
  laptop.addChild(TreeNode('macbook'))

  mobile = TreeNode('Mobile')
  mobile.addChild(TreeNode('iPhone'))
  mobile.addChild(TreeNode('pixel'))
  mobile.addChild(TreeNode('Vivo'))

  tv = TreeNode('TV')
  tv.addChild(TreeNode('Samsung'))
  tv.addChild(TreeNode('Bravia'))
  
  root.addChild(laptop)
  root.addChild(tv)
  root.addChild(mobile)

  return root

if __name__ == '__main__':
  root = build_product_tree()
  root.print_tree_level(1)
  pass