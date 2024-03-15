fn count(num: i32) {
    for num in num..=10 {
        println!("{}", num)
    }
}

fn count_down(mut num: i32) {
    while num > 1 {
        println!("{}", num)
        num = num -1;
    }
}   

fn main() {
    println!("Hello, world!");
    count(5);
    count_down(5);
}
