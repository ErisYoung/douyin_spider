class Handler(object):
    """
    Base Handler as super class
    """
    def handle(self, item, **kwargs):
        """
        handle one item,need subclass to implemented
        :param item:
        :param kwargs:
        :return:
        """
        return NotImplementedError
