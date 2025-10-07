package sdk

import "testing"

func TestBuildSignInput(t *testing.T) {
    signPath := "param2/1/x/y/100"
    params := map[string]string{"b": "2", "a": "1"}
    got := string(buildSignInput(signPath, params))
    want := "param2/1/x/y/100a1b2" // 先 path，再按键名排序拼 k+v
    if got != want {
        t.Fatalf("sign input mismatch: got %q want %q", got, want)
    }
}

