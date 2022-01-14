<?php

// Declare the class
class Path {
    // Declare tha variable for the current path
    protected $currentPath;

    // Function to get the current path in the declaration of the class
    public function __construct($path)
    {
        if ($this->checkPath($path)) {
            $this->currentPath = $path;
        } else {
            exit("The input path is not valid.");
        }
    }

    // Function to return the value of the current path
    public function getCurrentPath()
    {
        return $this->currentPath;
    }

    // Function to change directory
    public function cd($newPath)
    {
        $arrayNewPath = str_split($newPath);

        // Check if the user use '../' or just a full path
        if ($arrayNewPath[0] == '.' && $arrayNewPath[1] == '.') {

            $sliceNewPath = array_slice($arrayNewPath, 2);

            if ($this->checkPath(implode("", $sliceNewPath))) {
                $currentPathArray = str_split($this->currentPath) ;

                $newCurrentPath = array_slice($currentPathArray, 0, count($currentPathArray) - 2);

                $this->currentPath = implode("", array_merge($newCurrentPath, $sliceNewPath));
            } else {
                exit("The input path is not valid.");
            }
        } else {

            if ($this->checkPath($newPath)) {
                $this->currentPath = $newPath;
            } else {
                exit("The input path is not valid.");
            }
        }
    }

    // Function to check if the input path is valid
    private function checkPath($path)
    {
        $arrayPath = str_split($path);

        // Check if the first char is / and if the last is not / 
        if (ord($arrayPath[0]) != 47 || ord($arrayPath[count($arrayPath) - 1]) == 47) {
            return false;
        }

        // Check if all the char are valid
        foreach ($arrayPath as $index => $value) {
            if ($index % 2 == 0 && ord($value) != 47) {
                return false;
            }
            if ($index % 2 == 1 && !((ord($value) >= 65 && ord($value) <= 90) || (ord($value) >= 97 && ord($value) <= 122)) ) {
                echo $value . ord($value) . ' - ';
                return false;
            }
        }

        return true;
    }
}

$path = new Path('/a/b/c/d');
$path->cd('../x');
echo $path->getCurrentPath();
