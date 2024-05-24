import pytest
from src.school import Student, Teacher, ClassRoom, TooManyStudents


# Fixtures for testing
@pytest.fixture
def harry():
    return Student("Harry Potter")


@pytest.fixture
def hermione():
    return Student("Hermione Granger")


@pytest.fixture
def ron():
    return Student("Ron Weasley")


@pytest.fixture
def dumbledore():
    return Teacher("Albus Dumbledore")


@pytest.fixture
def snape():
    return Teacher("Severus Snape")


@pytest.fixture
def gryffindor_class(dumbledore, harry, hermione, ron):
    return ClassRoom(
        dumbledore, [harry, hermione, ron], "Defense Against the Dark Arts"
    )


# Test cases


def test_add_student(gryffindor_class, snape):
    new_student = Student("Draco Malfoy")
    gryffindor_class.add_student(new_student)
    assert new_student in gryffindor_class.students


def test_add_student_raises_exception(gryffindor_class):
    for i in range(7):
        gryffindor_class.add_student(Student(f"Student {i+4}"))

    with pytest.raises(TooManyStudents):
        gryffindor_class.add_student(Student("Extra Student"))


def test_remove_student(gryffindor_class):
    gryffindor_class.remove_student("Harry Potter")
    student_names = [student.name for student in gryffindor_class.students]
    assert "Harry Potter" not in student_names


def test_change_teacher(gryffindor_class, snape):
    gryffindor_class.change_teacher(snape)
    assert gryffindor_class.teacher == snape


@pytest.mark.parametrize(
    "student_name", ["Harry Potter", "Hermione Granger", "Ron Weasley"]
)
def test_remove_student_parameterized(gryffindor_class, student_name):
    gryffindor_class.remove_student(student_name)
    student_names = [student.name for student in gryffindor_class.students]
    assert student_name not in student_names


@pytest.mark.parametrize(
    "new_teacher", ["Severus Snape", "Minerva McGonagall", "Remus Lupin"]
)
def test_change_teacher_parameterized(gryffindor_class, new_teacher):
    new_teacher_obj = Teacher(new_teacher)
    gryffindor_class.change_teacher(new_teacher_obj)
    assert gryffindor_class.teacher.name == new_teacher
