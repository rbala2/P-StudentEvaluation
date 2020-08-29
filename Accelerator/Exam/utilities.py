from .models import AccResultsSummary, AccResults, AccQuestions , AccTests


# helper functions for exam evaluation
def evaluate_exam(student_id, session_id, testid):
    sobj = AccResultsSummary()
    robj = AccResults.objects.filter(session_id=session_id, student_id=student_id, testid=testid)
    tobj = AccTests.objects.filter(id=testid)

    total_score = 0
    answered_correct = 0
    answered_wrong = 0
    questions_attempted = len(robj)

    for rec in robj.values():
        qobj = AccQuestions.objects.filter(qno=rec['qno'])   # qobj should have only one record
        if qobj.values()[0]['answer'] == rec['answer_obj']:
            answered_correct += 1
            total_score = total_score + qobj.values()[0]['marks_carry']

    answered_wrong = questions_attempted - answered_correct

    val = float(tobj.values()[0]['negative_marking'])
    if val > 0 :
        total_score = total_score - answered_wrong * val
    sobj.pk = None
    sobj.test_start_time = rec['test_starttime']
    sobj.test_end_time = rec['test_endtime']
    sobj.test_result_status = 'NA'
    sobj.questions_attempted = questions_attempted
    sobj.answered_correct = answered_correct
    sobj.answered_wrong = answered_wrong
    sobj.session_id = session_id
    sobj.student_id = student_id
    sobj.testid = testid
    sobj.marks_obtained = total_score
    sobj.total_marks = tobj.values()[0]['total_marks']
    sobj.total_questions = tobj.values()[0]['total_questions']
    sobj.save()
    # TODO: need to add exceptions for failures when writing to DB to preserve the Exam data in file system (JSON format)
    # TODO: need to add a slider for question navigation on a page and timer visibility through out the page.


