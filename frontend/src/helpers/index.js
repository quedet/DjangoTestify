export const debounce = (fn, delay = 10) => {
    let timeoutId = null;
    return () => {
        clearInterval(timeoutId);
        timeoutId = setTimeout(fn, delay);
    };
};