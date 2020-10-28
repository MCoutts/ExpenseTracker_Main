# Team A: Kavan Adeshara, Dillon Hector, Matthew Coutts, Himani Vommi
# Team B: ZeZheng, Mis Champa

# class node

'''
#Item Node
# lets get started
#this holds our item here
'''


class itemNode:

    def __init__(self, name, cost=0):
        self.name = name
        self.cost = cost
        self.category = None  # level of need

    def setCost(self, c):
        self.cost = c

    def setCategory(self, cat):
        self.category = cat


'''
ListNode - this contains list of all listNodes
this gets passed to the expense tree

'''


class listNode:

    # initialize
    def __init__(self):

        self.l = []  # list of items held in a NODE (itemNode) | f(g(x))
        self.right = None
        self.left = None
        self.parent = None

    # function to append listNode
    def append(self, itemNode):
        self.l.append(itemNode)

    # function to get the total cost of the list
    def getTotal(self, total=0):

        for each in self.l:
            total += each.cost

        return total

    # function to acquire a specific item from the list: input by name
    def getItem(self, name):

        for item in self.l:
            if name == item.name:
                return item


'''
expense Tree sorts out the elements within the list
 left = cheap
  right = expensive
  BST oriented
'''


class expenseTree:

    # insert func to insert the data according to it's amount
    def tree(self, data):
        if data == self.data:
            return

        # if the data inserted is less than cur value itll
        # go into the left node
        if data < self.data:
            if self.left:
                self.left.tree(data)
            else:
                self.left = self.tree(data)


        # if the data is greater than the value
        # of the current node then it goes right
        else:
            if self.right:
                self.right.buildSTree(data)
            else:
                self.right = self.tree(data)

    # this will first visit left node
    # then the root node and finally
    # the right node and display them in
    # specific order

    def inOrderTrav(self):
        elements = []
        if self.left:  ###left
            elements += self.left.inOrderTrav()  # left

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTrav()
        return elements

    def insert(self, val):

        if self.root == None:
            self.root = Node(val)
        else:
            self.__insert(val, self.root)

    def __insert(self, val, currNode):

        if val < currNode.val:

            if currNode.leftChild == None:
                currNode.leftChild = Node(val, parent=currNode)
                self.updateBalanceFactor(currNode)
                self.checkForBalanace(currNode)
            else:
                self.__insert(val, currNode.leftChild)

        elif val > currNode.val:

            if currNode.rightChild == None:
                currNode.rightChild = Node(val, parent=currNode)
                self.updateBalanceFactor(currNode)
                self.checkForBalanace(currNode)
            else:
                self.__insert(val, currNode.rightChild)

        else:
            return "value already exist"

    # getItem from itemNode
    # parameters: name of the item
    def getItem(self, name):
        for each in self.l
            if name == item.name:
                return item
        # need a function to search for a specific item in the list node
        # need a helper function to traverse all the list nodes

    #  func getMaxCost
    def getMaxCost(self, max=0):
        # current = self
        # if self is None:
        #     return None
        # if self > max:
        #     self = max
        # return max
        pass

    # this find the minimum cost node
    def getMinCost(self, minimum=0):
        # if self is None: #if self = None then exit
        #     return None
        # current = self.root #temp val set to self.root
        # #idk if these even works imma cry
        # if current < self.root: # if current < self.root node
        #     if self < current: # and self is < current
        #         self = minimum #self is le minimum
        pass

    # insert func to insert the data according to it's amount

    def buildSTree(self, data):
        if data == self.data:
            return

        # if the data inserted is less than cur value itll
        # go into the left node
        if data < self.data:
            if self.left:
                self.left.buildSTree(data)
            else:
                self.left = self.BST(data)

        # if the data is greater than the value
        # of the current node then it goes right
        else:
            if self.right:
                self.right.buildSTree(data)
            else:
                self.right = self.BST(data)

    # this will first visit left node
    # then the root node and finally
    # the right node and display them in
    # specific order*


class Classifier:
    # luxury
    #
    pass


sampleList = listNode()
sampleList.append(3)

print(sampleList.getTotal)
l)