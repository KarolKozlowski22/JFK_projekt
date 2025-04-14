; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.3948252993100881646" = internal constant [3 x i8] c"%d\00"
@".str.1444584550978747635" = internal constant [3 x i8] c"%f\00"
define void @"main"()
{
entry:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  %"b" = alloca i32
  store i32 0, i32* %"b"
  %".4" = load i32, i32* %"a"
  %".5" = load i32, i32* %"b"
  %".6" = and i32 %".4", %".5"
  %"c" = alloca i32
  store i32 %".6", i32* %"c"
  %".8" = load i32, i32* %"a"
  %".9" = load i32, i32* %"b"
  %".10" = or i32 %".8", %".9"
  %"d" = alloca i32
  store i32 %".10", i32* %"d"
  %".12" = load i32, i32* %"a"
  %".13" = load i32, i32* %"b"
  %".14" = xor i32 %".12", %".13"
  %"e" = alloca i32
  store i32 %".14", i32* %"e"
  %".16" = load i32, i32* %"c"
  %".17" = bitcast [3 x i8]* @".str.3948252993100881646" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %".16")
  %".19" = load i32, i32* %"d"
  %".20" = bitcast [3 x i8]* @".str.3948252993100881646" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %".19")
  %".22" = load i32, i32* %"e"
  %".23" = bitcast [3 x i8]* @".str.3948252993100881646" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %".22")
  ret void
}
