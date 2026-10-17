func hasDuplicate(nums []int) bool {
    unique_nums := make(map[int]bool)
    for _, num := range nums {
        if unique_nums[num] {
            return true
        }
        unique_nums[num] = true 
    }
    return false
}
