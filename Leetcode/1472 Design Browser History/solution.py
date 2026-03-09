class ListNode:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.cur = self.head

    def visit(self, url: str) -> None:
        newnode = ListNode(url)
        newnode.prev = self.cur
        self.cur.next = newnode
        self.cur = newnode

    def back(self, steps: int) -> str:
        while self.cur.prev != None and steps > 0:
            self.cur = self.cur.prev
            steps -= 1

        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next != None and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        
        return self.cur.val
        