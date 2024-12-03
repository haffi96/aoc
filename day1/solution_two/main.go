package main

import (
	"aoc/common"
	"fmt"
	"log/slog"
	"os"
	"strings"
)

func main() {
	// Current working directory
	projectRoot, _ := os.Getwd()

	lines := common.ReadFileLines(fmt.Sprintf("%s/day1/input.txt", projectRoot))

	var leftIdMap = make(map[int]int)
	var totalScore int

	for _, line := range lines {

		split_line := strings.Fields(line)

		left := common.ConvertToInt(split_line[0])
		_ = common.ConvertToInt(split_line[1])

		// Check if left list value in map
		_, ok := leftIdMap[left]

		if ok {
			// Do nothing
		} else {
			// Add left value to both maps if not exists
			leftIdMap[left] = 1
		}
	}

	for _, line := range lines {
		split_line := strings.Fields(line)

		_ = common.ConvertToInt(split_line[0])
		right := common.ConvertToInt(split_line[1])

		// Check if right value in map
		if _, ok := leftIdMap[right]; ok {
			// increment counter of occurence
			prevScoreForVal := right * leftIdMap[right]

			leftIdMap[right] += 1
			// update similarity newScoreForVal
			newScoreForVal := right * leftIdMap[right]

			// Add to total score
			totalScore += newScoreForVal - prevScoreForVal
		}
	}

	slog.Info(fmt.Sprintf("Total score value: %v", totalScore))
}
