fn main() {


    
    
}




fn nested_function(a:i32) -> impl Fn(i32)->i32 {
return |b|b;
}

fn nested_2(a:i32) -> impl Fn(i32) -> i32{


move |x| a+x


}
mod tests {

    use super::*;
    #[test]
    fn test_nestor(){

        assert_eq!(nested_function(2)(3),3);

    }

    #[test]
    fn identity(){

        let x  = |x:i32|x;
        assert_eq!(x(1),1);
    }
}