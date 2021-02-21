

weight = .1
alpha = 0.01 # Alhpa is a penalty that prevents a zero update.


def neural_network(input, weight):

     prediction = input * weight
     return prediction

number_of_toes  = [8.5]

win_or_lose_binary = [1]

input = number_of_toes[0]
goal_pred = win_or_lose_binary[0]

pred = neural_network(input, weight) 

error = (pred - goal_pred) ** 2

delta = pred - goal_pred

weight_delta = input * delta 

weight -= weight_delat * alpha6
