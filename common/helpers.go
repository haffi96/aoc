package common

import (
	"os"
	"strconv"
	"strings"
)

func AbsInt(x int) int {
	return AbsDiffInt(x, 0)
}

func AbsDiffInt(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}

func AbsDiffUint(x, y uint) uint {
	if x < y {
		return y - x
	}
	return x - y
}

func Check(e error) {
	if e != nil {
		panic(e)
	}
}

func ConvertToInt(val string) int {
	intVal, err := strconv.Atoi(val)
	Check(err)
	return intVal
}

func ReadFileLines(filePath string) []string {
	data, err := os.ReadFile(filePath)

	Check(err)

	lines := strings.Split(string(data), "\n")

	return lines
}
