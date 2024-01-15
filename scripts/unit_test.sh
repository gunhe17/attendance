PYTHONPATH=. pytest -v \
    ./test/attendance/domain/article/test_article.py \
    ./test/attendance/domain/article/test_article_name.py \
    ./test/attendance/domain/article/test_size.py \
    ./test/attendance/domain/article/test_threshold.py \

PYTHONPATH=. pytest -v \
    ./test/attendance/domain/student/test_age.py \
    ./test/attendance/domain/student/test_group.py \
    ./test/attendance/domain/student/test_student_name.py \
    ./test/attendance/domain/student/test_student.py \
    ./test/attendance/domain/student/test_team.py \
    ./test/attendance/domain/student/test_tell_num.py \