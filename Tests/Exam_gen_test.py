"""
Test file, contains the test functions for testing Exam_gen
"""
import pytest


@pytest.fixture     # Define an exam class instance to be used in the tests
def Exam():
    from src.Exam_gen.Exam_Generator import Generate_Exam
    Exam = Generate_Exam(6)
    return Exam


def test_leitner_topup_algos():     # Check if the right number of question is selected
    from src.Compatibility_script import data_bank
    from src.Exam_gen.Leitner_Algo import leitner_algo, topup_algo
    import datetime

    nb_of_q = 5
    e_questions = []
    t = datetime.datetime.now()
    leitner_algo(data_bank, nb_of_q, e_questions, t)
    topup_algo(e_questions, nb_of_q, data_bank)
    assert len(e_questions) == nb_of_q


def test_select_questions(Exam):    # Check if the selection process is successful
    Exam.select_questions()
    assert len(Exam.e_questions) == 6

# Check if length of Attempts_log = og log length + right number for new attempts
# def test_attempts_append(og_log_len, nb_of_q):
#     with open('Attempts_log.txt', "r") as Attempts_log:
#         assert len(Attempts_log.readlines()) == (og_log_len + nb_of_q)

# def test_check_key(attempt, attempt_count):

