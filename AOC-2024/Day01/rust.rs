fn parse_input(input: &str) -> Vec<(u64, u64)> {
    input
        .lines()
        .filter_map(|line| {
            let numbers: Vec<u64> = line
                .split(|c: char| !c.is_digit(10) && c != '-')
                .filter_map(|x| x.parse::<u64>().ok())
                .collect();
            if numbers.len() >= 2 {
                Some((numbers[0], numbers[1]))
            } else {
                None
            }
        })
        .collect()
}
