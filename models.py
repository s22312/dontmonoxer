from typing import get_type_hints

class ModelBase:
    def __init__(self, data: object) -> None:
        vars(self).update(data)
        for k, v in get_type_hints(self.__class__).items():
            vars(self).update({k: v(data.get(k))})

class ClassInfo(ModelBase):
    id: int
    schoolId: int
    kind: int
    visibility: int
    capacity: int
    order: int
    icon: str
    name: str
    description: str
    orgId: int
    createdAt: str
    updatedAt: str

class SchoolInfo(ModelBase):
    id: int
    kind: int
    visibility: int
    capacity: int
    icon: str
    name: str
    description: str
    createdAt: str
    updatedAt: str
    mode: int
    orgId: int

class TaskInfo(ModelBase):
    id: int
    classId: int
    bookId: int
    planId: int
    start: str
    order: int
    comment: str
    status: int
    createdAt: str
    updatedAt: str

class BookInfo(ModelBase):
    id: int
    userId: int
    name: str
    subTitle: str
    description: str
    createdAt: str
    updatedAt: str
    icon: str
    status: int
    visibility: int
    ownerId: int
    ownerType: int
    bookType: int

class StudyPlan(ModelBase):
    id: int
    bookId: int
    userId: int
    orgId: int
    status: int
    recoverDelayStrategy: int
    advanceStrategy: int
    dayCount: int
    changeTime: str
    bookStatus: int
    periodLength: int
    forwardAmount: int
    offDayOfWeek: int
    start: str
    ownerId: int
    ownerType: int
    createdAt: str
    updatedAt: str

class PlanInfo(ModelBase):
    studyPlan: StudyPlan
    classRole: int
    days: list[any]

class Task(ModelBase):
    task: TaskInfo
    book: BookInfo
    tags: list[any]
    planInfo: PlanInfo

class Class(ModelBase):
    clazz: ClassInfo
    school: SchoolInfo
    tasks: list[Task]
    threads: list[any]
    threadCount: int
    memberCount: int
    adminThreads: list[any]
    schoolRole: int
    classRole: int