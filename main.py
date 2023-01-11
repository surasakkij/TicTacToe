from State import State
from Player import Player
from HumanPlayer import HumanPlayer

if __name__ == "__main__":
    # training
    # p1 = Player("p1")
    # p2 = Player("p2")

    # st = State(p1, p2)
    # print("training...")
    # st.play(50000)

    # p1.savePolicy()
    # p2.savePolicy()

    #play with human
    p1 = Player("computer", exp_rate=0)
    p1.loadPolicy("policy_p1")

    p2 = HumanPlayer("human")

    st = State(p1, p2)
    st.play2()