package body Ada12 is
   function Max (X, Y : Integer) return Integer is
     (if X > Y then X else Y);
end Ada12;
