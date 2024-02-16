# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] =0.278071

    level1["cough"] = -1.0
    level1["cough_info_gain"] =0.034851

    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.236452

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.029049

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = 0.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = 0.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.072905

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.721928

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.170950

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] =0.721928

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.3219

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.170950

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    tree=u.BinaryTree("smoking")
    A=tree.insert_left("cough")
    B=tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    answer["tree"] = tree  
    answer["training_error"] = 0.0   

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}
    #question_a
    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.425364
    # Infogain
    answer["(b) x < 0.2"] = 0.177392
    answer["(b) x < 0.7"] = 0.355702
    answer["(b) y < 0.6"] = 0.347818

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] =  'x<=0.7'

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("x<=0.7")
    
    A=tree.insert_left("y<=0.6")
    A.insert_left("B")
    C=A.insert_right("x<=0.2")
    D=C.insert_left("y<=0.8")
    C.insert_right("A")
    D.insert_left("C")
    D.insert_right("B")
    
    B=tree.insert_right("y<=0.6")
    E=B.insert_left("y<=0.3")
    B.insert_right("A")
    E.insert_left("A")
    E.insert_right("C")
    answer["(d) full decision tree"] = tree
    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.162500
    answer["(e) Gini, Shirt type"] = 0.491428

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "Observing the above gini impurity measures, it looks like ID best suites for the first split (root). But in general using ID as root doesn't produce valid/consistent results on unseen/test set. So we have to choose the next least impurity. which was Using Car Type for the first decision"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualitative','ordinal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "If time is AM or PM we say it has just 2 values so Binary"

    answer["b"] = ["continuous", "qunatitative", "ratio"]
    answer["b: explain"] = "(0 light year if it doesn;t take time, 6 light years is 2 times of 3 light years)"

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = ""

    answer["d"] = ["contiuous", "qunatitaive", "ratio"]
    answer["d: explain"] = "5 +5 and 2*5 both can make 10 angle"

    answer["e"] = ["discrete", "qualitative", "ordinal"]
    answer["e: explain"] = ""

    answer["f"] = ["continuous", "quantitative", "interval"]
    answer["f: explain"] = ""

    answer["g"] = ["discrete", "quantitative", "ratio"]
    answer["g: explain"] = ""

    answer["h"] = ["discrete", "qualitative", "nominal"]
    answer["h: explain"] = ""

    answer["i"] = ["discrete", "qualitative", "nominal"]
    answer["i: explain"] = "If we doesn't consider the fact that the one that passes the more amount light is higher and ectera, if we consider this into account it will be ordinal"

    answer["j"] = ["discrete", "qualitative", "ordinal"]
    answer["j: explain"] = ""

    answer["k"] = ["continuous", "quantitative", "ratio"]
    answer["k: explain"] = "In google maps if we say we are 0 feet away which means which indicates absolute 0, also you can say hcb is twice as far as union which indicates its a ratio"

    answer["l"] = ["continuous", "quantitative", "ratio"]
    answer["l: explain"] = ""

    answer["m"] = ["discrete", 'qualitative', "nominal"]
    answer["m: explain"] = ""

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Its because if a model perform 98'%' accuracy on trainset and 72'%' on test set, it indicates there is a lot of variance, indicates model might have overfitted on trainset. And in case of Model 2 we dont have such a high variance and low bias problem, as it performs reasonbly good on both sets"

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Performance is almost the same 81 and 85 not much of a difference, occams Razor states that if model have identical performance, choose the one that has low complexity (here pruned model [model 2]) as it(pruning) ensures model from getting overfit."

    explain["c similarity"] = "Complexity Term"
    explain["c similarity explain"] = "If the model is complex (either depth or number of leaves), the complexity term in both the calculations(MDL and pessimistic) will penalize the error in the same direction. In case of Pessimistic if K is more, the penalty will be higher. Also in case of MDL when the children are high, the complexity increases."

    explain["c difference"] = "Representation of Weights and Errors"
    explain["c difference explain"] = "In MDL values are represent using bits, where as its not the same in case of Pessimistic Error"

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x<=0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y<=0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x<=0.2"

    # When we move to right node of y =0.4
    # We pruned the tree (2 level) as class B, because only 6%(0.2*0.3) of A's will go through that decision, And rest all the A's have their own 
    err=0.2*0.3
    answer["b, expected error"] = err

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x<=0.5")
    A=tree.insert_left("y<=0.4")
    C=A.insert_left('A')
    A.insert_right('x<=0.2')

    B=tree.insert_right("A")
    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531004

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.231378
    answer["e, gain ratio, Handedness"] = 0.531004

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

