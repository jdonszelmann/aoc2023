use std::collections::hash_map::Entry;
use std::collections::HashMap;

pub trait UpdateWith<T>: Sized {
    fn update_with(self, f: impl FnOnce(T) -> T);

    fn update_with_val(self, value: T, f: impl FnOnce(T, T) -> T) {
        self.update_with(|a| f(a, value))
    }
}

impl<T: Copy> UpdateWith<T> for &mut T {
    fn update_with(self, f: impl FnOnce(T) -> T) {
        *self = f(*self)
    }
}
