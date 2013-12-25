from Card import Card

class CardSet(list):

    def __contains__(self, obj):
        """Surchage in pour CardSet"""
        seq = list(self)

        tmp = obj
        for _ in range(4):
            tmp = tmp.rotate_right()
            if tmp in seq:
                return True
            
        return False

    def init_crazy_turle_cardset(self):
        """Init avec les cartes presentes sur le Crazy Turtle Solver d'internet"""
        self.append(Card("TJTBTVCR"))
        self.append(Card("TBTRCBCV"))
        self.append(Card("TVTRCJCR"))
        self.append(Card("TBCVCJCV"))
        self.append(Card("TRTVCBCJ"))
        self.append(Card("CVTJTRTR"))
        self.append(Card("TJCBTJCR"))
        self.append(Card("TJCJCRTB"))
        self.append(Card("CVCBTVCB"))
