from flask import render_template, redirect, session, request
from sudoku_app import app
from sudoku_app.models.board import Board

#---------------Display Methods------------------#
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sudoku")
def sudoku():
    return render_template("sudoku.html", start_board = Board.get_board())
    
@app.route("/solution")
def solution():
    return render_template("solution.html", solutions = Board.solve_board())

#--------------Action Methods--------------------#
@app.route("/board/solve")
def solve_board():
    pass

@app.route("/board/new")
def new_board():
    pass
