pub trait FoldMut: Iterator {
    fn fold_mut<B, F>(mut self, init: B, mut f: F) -> B
    where
        Self: Sized,
        F: FnMut(&mut B, Self::Item),
    {
        self.fold(init, |mut acc, val| {
            f(&mut acc, val);
            acc
        })
    }
}

impl<T> FoldMut for T where T: Iterator {}
