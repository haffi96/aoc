package main

import (
	"aoc/common"
	"fmt"
	"log/slog"
	"os"
	"slices"
	"strings"
)

func main() {
	// Current working directory
	projectRoot, _ := os.Getwd()

	lines := common.ReadFileLines(fmt.Sprintf("%s/day1/input.txt", projectRoot))

	var left_array []int
	var right_array []int

	for _, line := range lines {
		split_line := strings.Fields(line)

		left := common.ConvertToInt(split_line[0])
		right := common.ConvertToInt(split_line[1])

		left_array = append(left_array, left)
		right_array = append(right_array, right)
	}

	slices.Sort(left_array)
	slices.Sort(right_array)

	var diffCounter int
	for i := range left_array {
		diffCounter += common.AbsDiffInt(left_array[i], right_array[i])
	}

	slog.Info(fmt.Sprintf("Total diff: %v ", diffCounter))
}
