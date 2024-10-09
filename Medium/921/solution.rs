impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut oc = 0;
        let mut cc = 0;

        for c in s.chars(){
            if c == '(' {
                oc += 1;
            }else if c == ')' && oc > 0 {
                oc -= 1;
            }else {
                cc += 1
            }
        }
        oc + cc
    }
}