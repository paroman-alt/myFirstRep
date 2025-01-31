#хук по проверке соответствия названия коммита таску указанному в названии ветки
#поиск символа "/" справа налево в названии ветки и запись символов правее
def valid_commit_check(branch_name):
    commit_name = ""
    for i in range(len(branch_name)):
        if branch_name[-i] == "/":
            print(-i)
            break

        commit_name = branch_name[i] + commit_name
    if 'task' in branch_name:

#comment 00001090909


    return commit_name

print(valid_commit_check("feature/task-033"))