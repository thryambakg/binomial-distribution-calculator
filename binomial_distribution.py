import streamlit as st

trials = st.text_input("enter the number of trials: ")
successes = st.text_input("enter the number of desired successes: ")
probability = st.text_input("enter the probability of success (decimal): ")

trialsNum = int(trials)
successesNum = int(successes)
probabilityNum = float(probability)

multNum = trialsNum - 1
trialsFact = trialsNum
for i in range(multNum):
    trialsFact = trialsFact * multNum 
    multNum = multNum - 1

multNum2 = successesNum - 1
successesFact = successesNum
for i in range(multNum2):
    successesFact = successesFact * multNum2
    multNum2 = multNum2 - 1

difference = trialsNum - successesNum
multNum3 = difference - 1
differenceFact = difference
for i in range(multNum3):
    differenceFact = differenceFact * multNum3
    multNum3 = multNum3 - 1

combinations = trialsFact / (successesFact * differenceFact)

probabilitySuccess = probabilityNum ** successesNum

probabilityFail = (1 - probabilityNum) ** (trialsNum - successesNum)

ans = combinations * probabilitySuccess * probabilityFail

st.write(ans) 