from datetime import datetime, timedelta
import unittest

from app.controllers.quizzes_controller import QuizzesController  # Changed 'QuizzesController' to 'QuizController'


class TestQuizFunctionality(unittest.TestCase):  # Changed 'QuizzesTest' to 'TestQuizFunctionality'

    def setUp(self):
        # Setting up the environment for testing with non-production data
        self.quiz_ctrl = QuizzesController('quizzes_test.py')  # Changed 'ctrl' to 'quiz_ctrl'

    # The error occurs at line 94 of "quizzes_controller.py"
    def test_failure_case_01(self):
        # Initializing input parameters for add_quiz function
        title = "Quiz Title"
        text = "Quiz Text"
        available_datetime = datetime(2024, 5, 3, 0, 0, 0)
        due_datetime = datetime(2024, 5, 3, 11, 11, 11)

        # Fetch quiz_id from add_quiz function
        quiz_id = self.quiz_ctrl \
            .add_quiz(title=title,
                      text=text,
                      available_date=available_datetime,
                      due_date=due_datetime)

        # Fetch question_id from add_question function
        question_id = self.quiz_ctrl \
            .add_question(quiz_id,
                          title=title,
                          text=text)

        # Initializing input parametes for add_answer function
        is_correct = True
        # Initializing text parameter with a datetime value instead of expected string type
        answer_text = datetime.now()

        # Fetching answer_id from add_answer function
        # Throws TypeError as datetime was passed instead of expected string
        answer_id = self.quiz_ctrl \
            .add_answer(question_id=question_id,
                        text=answer_text,
                        is_correct=is_correct)

        # Assertion should fail as answer_id is None
        self.assertIsNone(answer_id, "answer_id is expected to be None")

    # The error occurs at line 81 of quiz_controller.py
    def test_failure_case_02(self):
        # Initializing input parameters for add_quiz function
        title = "Quiz Title"
        text = "Quiz Text"
        available_datetime = datetime(2024, 5, 3, 0, 0, 0)
        due_datetime = datetime(2024, 5, 3, 11, 11, 11)

        # Fetch quiz_id from add_quiz function
        quiz_id = self.quiz_ctrl \
            .add_quiz(title=title,
                      text=text,
                      available_date=available_datetime,
                      due_date=due_datetime)

        # Initializing input parameter for add_question function
        # Initializing title with datetime value instead of expected string datatype
        title = datetime(2024, 5, 3, 8, 8, 8)

        # Fetch question_id from add_question function
        # Throws TypeError as title is not Serializable
        question_id = self.quiz_ctrl \
            .add_question(quiz_id=quiz_id,
                          title=title,
                          text=text)

        # Should not reach here due to TypeError
        self.assertIsNone(question_id, "Expected result to be None")

    # The error occurs at line 63 of quiz_controller.py
    def test_failure_case_03(self):
        # Initializing input parameters for add_quiz function
        # Initializing title with integer value instead of expected string value
        title = 1
        text = "Quiz Text"
        available_datetime = datetime(2024, 5, 3, 0, 0, 0)
        due_datetime = datetime(2024, 5, 3, 11, 11, 11)

        # Fetch quiz_id from add_quiz function
        # Throws unsupported operand type exception
        quiz_id = self.quiz_ctrl \
            .add_quiz(title=title,
                      text=text,
                      available_date=available_datetime,
                      due_date=due_datetime)

        # Assert quiz_id is null
        self.assertIsNone(quiz_id, "Quiz Id is None")


if __name__ == '__main__':
    unittest.main()
