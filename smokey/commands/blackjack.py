
import random


class BlackjackGame:

    def __init__(self, user_id="Player"):
        self.user_id = user_id
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        self.winner = None

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K", "A"
        ]

        self.deck = []

        for suit in suits:
            for rank in ranks:
                value = 10 if rank in ["J", "Q", "K"] else (
                    11 if rank == "A" else int(rank)
                )

                self.deck.append({
                    "rank": rank,
                    "suit": suit,
                    "value": value
                })

        random.shuffle(self.deck)

    def calculate_score(self, hand):
        score = sum(card["value"] for card in hand)
        aces = sum(card["rank"] == "A" for card in hand)

        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score

    def deal_cards(self):
        self.create_deck()

        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]

        self.game_over = False
        self.winner = None

        if self.calculate_score(self.player_hand) == 21:
            self.stand()

        return self.get_status()

    def hit(self):
        if self.game_over:
            return self.get_status()

        self.player_hand.append(self.deck.pop())

        if self.calculate_score(self.player_hand) > 21:
            self.game_over = True
            self.winner = "Dealer"

        return self.get_status()

    def stand(self):
        if self.game_over:
            return self.get_status()

        while self.calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())

        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

        if dealer_score > 21 or player_score > dealer_score:
            self.winner = "Player"
        elif player_score < dealer_score:
            self.winner = "Dealer"
        else:
            self.winner = "Tie"

        self.game_over = True

        return self.get_status()

    def format_hand(self, hand):
        return ", ".join(
            f'{card["rank"]} of {card["suit"]}'
            for card in hand
        )

    def get_status(self):
        player_score = self.calculate_score(self.player_hand)

        if not self.game_over:
            dealer_showing = self.dealer_hand[0]

            return (
                f"Player: {self.format_hand(self.player_hand)}\n"
                f"Player score: {player_score}\n"
                f"Dealer showing: {dealer_showing['rank']} "
                f"of {dealer_showing['suit']}\n"
                "Choose Hit or Stand."
            )

        dealer_score = self.calculate_score(self.dealer_hand)

        return (
            "BLACKJACK GAME OVER\n"
            f"Player hand: {self.format_hand(self.player_hand)}\n"
            f"Player score: {player_score}\n"
            f"Dealer hand: {self.format_hand(self.dealer_hand)}\n"
            f"Dealer score: {dealer_score}\n"
            f"Winner: {self.winner}"
        )
