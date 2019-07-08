# Sudoku - A backtracking graph coloring based strategy

This project is responsible for solving the Sudoku game with a backtracking graph coloring based strategy. The configuration can be changed on *config* file and there are some test files on examples folder.

## Running

* Execute the strategy:

```
python3 main.py -i {input}


    * input: Input file path
```

* Output:

<center>
0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;6&ensp;&ensp;8&ensp;&ensp;0&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;1&ensp;&ensp;7&ensp;&ensp;2&ensp;&ensp;5&ensp;&ensp;4&ensp;&ensp;9&ensp;&ensp;6&ensp;&ensp;8&ensp;&ensp;3<br/>
0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;7&ensp;&ensp;3&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;9&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;6&ensp;&ensp;4&ensp;&ensp;5&ensp;&ensp;8&ensp;&ensp;7&ensp;&ensp;3&ensp;&ensp;2&ensp;&ensp;1&ensp;&ensp;9<br/>
3&ensp;&ensp;0&ensp;&ensp;9&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;4&ensp;&ensp;5&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;3&ensp;&ensp;8&ensp;&ensp;9&ensp;&ensp;2&ensp;&ensp;6&ensp;&ensp;1&ensp;&ensp;7&ensp;&ensp;4&ensp;&ensp;5<br/>
4&ensp;&ensp;9&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;4&ensp;&ensp;9&ensp;&ensp;6&ensp;&ensp;3&ensp;&ensp;2&ensp;&ensp;7&ensp;&ensp;8&ensp;&ensp;5&ensp;&ensp;1<br/>
8&ensp;&ensp;0&ensp;&ensp;3&ensp;&ensp;0&ensp;&ensp;5&ensp;&ensp;0&ensp;&ensp;9&ensp;&ensp;0&ensp;&ensp;2&ensp;&ensp;&ensp;&ensp;->&ensp;&ensp;&ensp;&ensp;8&ensp;&ensp;1&ensp;&ensp;3&ensp;&ensp;4&ensp;&ensp;5&ensp;&ensp;6&ensp;&ensp;9&ensp;&ensp;7&ensp;&ensp;2<br/>
0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;3&ensp;&ensp;6&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;2&ensp;&ensp;5&ensp;&ensp;7&ensp;&ensp;1&ensp;&ensp;9&ensp;&ensp;8&ensp;&ensp;4&ensp;&ensp;3&ensp;&ensp;6<br/>
9&ensp;&ensp;6&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;3&ensp;&ensp;0&ensp;&ensp;8&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;9&ensp;&ensp;6&ensp;&ensp;4&ensp;&ensp;7&ensp;&ensp;1&ensp;&ensp;5&ensp;&ensp;3&ensp;&ensp;2&ensp;&ensp;8<br/>
7&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;6&ensp;&ensp;8&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;7&ensp;&ensp;3&ensp;&ensp;1&ensp;&ensp;6&ensp;&ensp;8&ensp;&ensp;2&ensp;&ensp;5&ensp;&ensp;9&ensp;&ensp;4<br/>
0&ensp;&ensp;2&ensp;&ensp;8&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;0&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;5&ensp;&ensp;2&ensp;&ensp;8&ensp;&ensp;9&ensp;&ensp;3&ensp;&ensp;4&ensp;&ensp;1&ensp;&ensp;6&ensp;&ensp;7<br/>
</center>

## Authors

* **Gleyberson Andrade** - [gleybersonandrade](https://github.com/gleybersonandrade)

## License

This project is licensed under the MIT License.
