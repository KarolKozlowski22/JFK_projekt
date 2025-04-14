; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.7951315541544645107" = internal constant [3 x i8] c"%d\00"
@".str.6650026928202722788" = internal constant [3 x i8] c"%f\00"
define void @"main"()
{
entry:
  %"x" = alloca i32
  store i32 0, i32* %"x"
  %".3" = bitcast [3 x i8]* @".str.7951315541544645107" to i8*
  %".4" = call i32 @"fflush"(i8* null)
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"x")
  %".6" = load i32, i32* %"x"
  %".7" = bitcast [3 x i8]* @".str.7951315541544645107" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  ret void
}

declare i32 @"fflush"(i8* %".1")
