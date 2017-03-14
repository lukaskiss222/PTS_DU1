import login
import database
import commands
login = login.Login()
database = database.Database("database.db")
history = commands.CommandHistory()
while True:
    command = input("Enter Command:>")
    if command.startswith("quit"):
        temp = commands.CommandQuit(database)
    elif command.startswith("points "):
        para = command.split(" ")
        temp = commands.CommandPoints(database, para[1], int(para[2]))
    elif command.startswith("reduce "):
        para = command.split(" ")
        temp = commands.CommandReduce(database, int(para[1]))
    elif command.startswith("junior"):
        para = command.split(" ")
        temp = commands.CommandJunior(database, para[1])
    elif command.startswith("ranking junior"):
        temp = commands.CommandRankingJunior(database)
    elif command.startswith("ranking"):
        temp = commands.CommandRanking(database)
    history.addAndExecute(temp)
